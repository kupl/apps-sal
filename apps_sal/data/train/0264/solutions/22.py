class Solution(object):
    def maxLength(self, arr):
        def get_max_len(arr):

            # start with unique elements in given list
            dp = [set(x) for x in arr if len(set(x)) == len(x)]

            for v in arr:
                # check for duplicates
                if len(a := set(v)) == len(v):
                    # concat to each valid set in list
                    for b in dp:
                        # skip if sets share letters
                        if a & b:
                            continue
                        # combine sets, add to dp
                        dp.append(a | b)
            # remove initial sets because we need to concatenate
            #for x in arr: 
            #    if (tmp := set(x)) in dp:
            #       dp.remove(tmp)
            # make sure we have valid answer
            return max(len(x) for x in dp) if dp else 0
        return get_max_len(arr)  
