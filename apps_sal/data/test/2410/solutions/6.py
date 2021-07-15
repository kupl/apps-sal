def mi():
        return list(map(int, input().split()))
'''
3
4
1 2 3 4
3
7 4 -1
3
5 -5 5
'''


def maxSubArraySum(a, size):
    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far

for _ in range(int(input())):
        n = int(input())
        a = list(mi())
        ade = max(maxSubArraySum(a,n-1), maxSubArraySum(a[1:],n-1))
        if sum(a)>ade:
                print ('YES')
        else:
                print ('NO')

