print("Yes" if "TTT" in ''.join(["T" if p else "F" for p in [len(list(set(list(map(int, input().split()))))) == 1 for l in range(int(input()))]]) else "No")
