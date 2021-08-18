

n, k, m = list(map(int, input().split()))
a = list(map(int, input().split()))

a = sum(a)

score = (n * m) - a

if score <= k:
    answer = score if score > 0 else "0"
    print(answer)
else:
    print("-1")
