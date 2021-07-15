import sys
K = int(input())
a = 7%K

if a==0:
    print(1)
    return

for i in range(1,K):
    a = (10 * a + 7)%K
    if a == 0:
        print(i+1)
        return

print(-1)
