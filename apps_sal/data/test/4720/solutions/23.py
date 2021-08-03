N = int(input())
people = 0
for i in range(N):
    l, r = list(map(int, input().split()))
    people += r - l + 1
print(people)
