n = int(input())
ai = list(map(int,input().split()))
num = sum(ai)
if num % 2 == 0:
    if sum(ai) < 2 * max(ai):
        print("NO")
    else:
        print("YES")
else:
    print("NO")

