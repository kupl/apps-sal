class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        win_list = [0, 0]
        for element in arr:
            if win_list[-1] < k:
                check_list = [arr[0], arr[1]]
                if check_list[0] > check_list[1]:
                    lost_ele = check_list[1]
                    if check_list[0] != win_list[0]:
                        win_list = [check_list[0], 1]
                    else:
                        win_list = [check_list[0], win_list[1] + 1]
                    arr.pop(1)
                    arr.append(lost_ele)
                else:
                    lost_ele = check_list[0]
                    if check_list[1] != win_list[0]:
                        win_list = [check_list[1], 1]
                    else:
                        win_list = [check_list[1], win_list[1] + 1]
                    arr.pop(0)
                    arr.append(lost_ele)
            else:
                break
        if win_list[-1] < k:
            result = win_list[0]
        else:
            result = win_list[0]
        return result
