import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


# def sub(kouho, target):
#     l = len(kouho)
#     best = None
#     for b in range(1<<l):
#         v = 0
#         for i in range(l.bit_length()):
#             if b>>i&1:
#                 v += 1<<i
#         if 
                

n = int(input())
a = list(map(int, input().split()))

val = 0
for num in a[2:]:
    val ^= num
k = a[0] + a[1]
if (k-val)%2!=0 or k<val:
    ans = -1
else:
    tmp = (k-val)//2
    if tmp<0 or 2*tmp>k:
        ans = -1
    else:
        v1 = tmp
        v2 = tmp
        kouho = []
        ans = None
        if tmp>a[0]:
            ans = -1
        diff = k - 2*tmp
        for i in range(diff.bit_length()):
            if (diff&1<<i) & tmp:
                ans = -1
                break
            elif diff&1<<i:
                kouho.append(1<<i)
        s = sum(kouho)
        if ans is None:
            for num in kouho[::-1]:
                s -= num
                if v2+s<a[1]:
                    v2 += num
                elif v1+num<=a[0]:
                    v1 += num
                else:
                    v2 += num
            if v1==0:
                ans = -1
            else:
                ans = a[0]-v1
        else:
            ans = -1
        
print(ans)
