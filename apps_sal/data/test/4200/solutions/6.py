n, m = map(int, input().split())
lst = list(map(int, input().split()))
sm = sum(lst)
if m <= sum([x >= sm / (4 * m) for x in lst]):
    print("Yes")
else:
    print("No")
