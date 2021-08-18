
import math


def abs(num):
    if num < 0:
        return -num
    else:
        return num


def abc163e(n, a):
    hap_dict = dict()
    hap_list = []
    for elem in range(n):
        if a[elem] in hap_dict:
            hap_dict[a[elem]].append(elem)
        else:
            tmp_list = [elem]
            hap_dict[a[elem]] = tmp_list
            hap_list.append(a[elem])

    hap_list.sort(reverse=True)

    left = 0
    right = n - 1

    num = 0
    dp = [[0 for re in range(n + 1)] for le in range(n + 1)]
    for hap in hap_list:
        pos_list = hap_dict[hap]

        while len(pos_list) != 0:
            tgt = pos_list.pop()

            num += 1

            for left in range(num + 1):
                right = num - left
                if left == num:
                    dp[left][right] = dp[left - 1][right] + hap * abs(tgt - left + 1)
                elif left == 0:
                    dp[left][right] = dp[left][right - 1] + hap * abs(n - right - tgt)
                else:
                    left_dp = dp[left - 1][right] + hap * abs(tgt - left + 1)
                    right_dp = dp[left][right - 1] + hap * abs(n - right - tgt)
                    dp[left][right] = max(left_dp, right_dp)

    ans_list = []
    for i in range(num + 1):
        ans_list.append(dp[i][num - i])
    return max(ans_list)


if(__name__ == '__main__'):
    n = int(input())
    a = list(map(int, input().split(" ")))

    ans = abc163e(n, a)

    print(ans)
