def solve():
    N = int(input())
    T = input()
    if N == 1:
        return 20_000_000_000 if T == "1" else 10_000_000_000
    T = T.replace("110", "T")
    if T.startswith("10"):
        T = "T" + T[2:]
    elif T.startswith("0"):
        T = "T" + T[1:]
    if T.endswith("11"):
        T = T[:-2] + "T"
    elif T.endswith("1"):
        T = T[:-1] + "T"
    if all(t == "T" for t in T):
        return 10_000_000_000 - (len(T) - 1)
    else:
        return 0


print(solve())
