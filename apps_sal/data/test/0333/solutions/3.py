#n = int(input())
#a, b = map(int, input())
a = input()
b = input()
#arr = list(map(int, input().split()))
if a != b:
    print(max(len(a), len(b)))
else:
    print(-1)
