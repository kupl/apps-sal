import sys

def div(n):
    count = 0
    for i in range(1, n+1):
        count += 1 if n%i==0 else 0
    return count

ans = 0
for i in range(1, int(input())+1):
    ans += 1 if i%2==1 and div(i) == 8 else 0
print(ans)
