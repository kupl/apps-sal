MAX = 999999999


def do():
    n = int(input())
    mx = MAX
    mn = -MAX
    change, thisDiv = list(map(int, input().split()))
    ratingChange = [0, change]
    divChange = [0, thisDiv]
    for i in range(n - 1):
        change, thisDiv = list(map(int, input().split()))
        ratingChange.append(ratingChange[-1] + change)
        divChange.append(thisDiv)
    for i in range(n):
        if divChange[i + 1] == 1:
            mn = max(1900 - ratingChange[i], mn)
        else:
            mx = min(1899 - ratingChange[i], mx)
        #print(mn, mx)
    if mn > mx:
        return "Impossible"
    else:
        if mx == MAX:
            return "Infinity"
        else:
            return str(mx + ratingChange[-1])


print(do())
