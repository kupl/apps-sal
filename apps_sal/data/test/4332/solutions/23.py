N = int(input())


def S(n: int) -> int:
    return sum(map(int, str(n)))


ans = str()
if N % S(N) == 0:
    ans = "Yes"
else:
    ans = "No"

print(ans)
