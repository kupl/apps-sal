def look_for_ascending(t_list, sub_array): 
    good_lists = 0
    for idx in range(0, len(sub_array)):
        if sub_array[idx] > t_list[-1]:
            if len(t_list) ==2:
                good_lists+=1
            else:
                good_lists+= look_for_ascending(t_list+[sub_array[idx]], sub_array[idx+1:])
    
    return good_lists

def look_for_descending(t_list, sub_array): 
    good_lists = 0
    for idx in range(0, len(sub_array)):
        if sub_array[idx] < t_list[-1]:
            if len(t_list) ==2:
                good_lists+=1
            else:
                good_lists+= look_for_descending(t_list+[sub_array[idx]], sub_array[idx+1:])
    
    return good_lists



class Solution:
    def numTeams(self, rating: List[int]) -> int:
        good=0
        for idx in range(len(rating)):
            good+=look_for_ascending([rating[idx]], rating[idx+1:]) + look_for_descending([rating[idx]], rating[idx+1:])
        return good
