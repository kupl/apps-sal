N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = input()
d = []
for i in range(N):
    if T[i] == "r":
        if i < K or d[i-K] != "p":
            d.append("p")
        else:
            d.append("a")
    elif T[i] == "s":
        if i < K or d[i-K] != "r":
            d.append("r")
        else:
            d.append("a")
    else:
        if i < K or d[i-K] != "s":
            d.append("s")
        else:
            d.append("a")
ans = d.count("r") * R + d.count("s") * S + d.count("p") * P
print(ans)
