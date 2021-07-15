import math
def i_input(): return int(input())


def i_map(): return list(map(int, input().split()))


def i_list(): return list(map(int, input().split()))


def i_row(N): return [int(input()) for _ in range(N)]


def i_row_list(N): return [list(map(int, input().split())) for _ in range(N)]

x,n= i_map()
pp=i_list()

nums=list(range(1000))
nums.append(-1)
for p in pp:
    nums[p]=10**3
ans=10**18
ch=10**18

for num in nums:
    if ch>abs(x-num):
        ch=abs(x-num)
        ans=num
print(ans)





