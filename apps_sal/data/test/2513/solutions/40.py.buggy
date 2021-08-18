n = int(input())
s = input()


def sw(sl, dp):
    for i in range(1, n - 1):
        if sl[i] == "o" and dp[i] == "S":
            dp[i + 1] = dp[i - 1]
        elif sl[i] == "o" and dp[i] == "W":
            if dp[i - 1] == "S":
                dp[i + 1] = "W"
            else:
                dp[i + 1] = "S"
        elif sl[i] == "x" and dp[i] == "S":
            if dp[i - 1] == "S":
                dp[i + 1] = "W"
            else:
                dp[i + 1] = "S"
        else:
            dp[i + 1] = dp[i - 1]


sl = list(s)
dp = [0] * n
dp[0] = "S"
dp[1] = "S"
sw(sl, dp)
if sl[0] == "o":
    if dp[n - 1] == "W":
        pass
    elif sl[n - 1] == "x":
        if dp[n - 2] == "S":
            pass
        else:
            res = ''.join(dp)
            print(res)
            return
    elif sl[n - 1] == "o":
        if dp[n - 2] == "S":
            res = ''.join(dp)
            print(res)
            return
        else:
            pass
else:
    if dp[n - 1] == "S":
        pass
    elif sl[n - 1] == "x":
        if dp[n - 2] == "W":
            pass
        else:
            res = ''.join(dp)
            print(res)
            return
    elif sl[n - 1] == "o":
        if dp[n - 2] == "W":
            res = ''.join(dp)
            print(res)
            return
        else:
            pass

dp = [0] * n
dp[0] = "S"
dp[1] = "W"
sw(sl, dp)
if sl[0] == "o":
    if dp[n - 1] == "S":
        pass
    elif sl[n - 1] == "x":
        if dp[n - 2] == "W":
            pass
        else:
            res = ''.join(dp)
            print(res)
            return
    elif sl[n - 1] == "o":
        if dp[n - 2] == "W":
            res = ''.join(dp)
            print(res)
            return
        else:
            pass
else:
    if dp[n - 1] == "W":
        pass
    elif sl[n - 1] == "x":
        if dp[n - 2] == "S":
            pass
        else:
            res = ''.join(dp)
            print(res)
            return
    elif sl[n - 1] == "o":
        if dp[n - 2] == "S":
            res = ''.join(dp)
            print(res)
            return
        else:
            pass

dp = [0] * n
dp[0] = "W"
dp[1] = "S"
sw(sl, dp)
if sl[0] == "o":
    if dp[n - 1] == "S":
        pass
    elif sl[n - 1] == "x":
        if dp[n - 2] == "S":
            pass
        else:
            res = ''.join(dp)
            print(res)
            return
    elif sl[n - 1] == "o":
        if dp[n - 2] == "S":
            res = ''.join(dp)
            print(res)
            return
        else:
            pass
else:
    if dp[n - 1] == "W":
        pass
    elif sl[n - 1] == "x":
        if dp[n - 2] == "W":
            pass
        else:
            res = ''.join(dp)
            print(res)
            return
    elif sl[n - 1] == "o":
        if dp[n - 2] == "W":
            res = ''.join(dp)
            print(res)
            return
        else:
            pass

dp = [0] * n
dp[0] = "W"
dp[1] = "W"
sw(sl, dp)
if sl[0] == "o":
    if dp[n - 1] == "W":
        pass
    elif sl[n - 1] == "x":
        if dp[n - 2] == "W":
            pass
        else:
            res = ''.join(dp)
            print(res)
            return
    elif sl[n - 1] == "o":
        if dp[n - 2] == "W":
            res = ''.join(dp)
            print(res)
            return
        else:
            pass
else:
    if dp[n - 1] == "S":
        pass
    elif sl[n - 1] == "x":
        if dp[n - 2] == "S":
            pass
        else:
            res = ''.join(dp)
            print(res)
            return
    elif sl[n - 1] == "o":
        if dp[n - 2] == "S":
            res = ''.join(dp)
            print(res)
            return
        else:
            pass

print(-1)
