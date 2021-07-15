import sys
input = sys.stdin.readline

N=int(input())
S=input().strip()

for i in range(1,N):
    if ord(S[i-1])<=ord(S[i]):
        continue
    else:
        print("YES")
        print(i,i+1)
        return

print("NO")

