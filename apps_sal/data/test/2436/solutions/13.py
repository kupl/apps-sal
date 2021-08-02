# When angry, count to four; when very angry, swear. Mark Twain
# by : Blue Edge - Create some chaos

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    i = 1
    ans = 0
    for x in a:
        if x <= i:
            ans = i
        i += 1
    print(ans + 1)
