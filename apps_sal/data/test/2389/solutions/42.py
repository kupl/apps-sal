# 実際にシミュレーションしていく方針で解く
N, A, B, C = list(map(int, input().split()))
d = {}
d["A"] = A
d["B"] = B
d["C"] = C
S = [input() for _ in range(N)]
ans = []
for i in range(N):
    s = S[i]
    if s == "AB":
        if d["A"] > d["B"]:
            d["A"] -= 1
            d["B"] += 1
            ans.append("B")
        elif d["A"] < d["B"]:
            d["B"] -= 1
            d["A"] += 1
            ans.append("A")
        else:  # 同じ場合
            if d["A"] == d["B"] == 0:
                print("No")
                return
            if N > i + 1:
                if "A" in S[i + 1]:
                    d["B"] -= 1
                    d["A"] += 1
                    ans.append("A")
                elif "B" in S[i + 1]:
                    d["A"] -= 1
                    d["B"] += 1
                    ans.append("B")
                else:
                    d["A"] -= 1
                    d["B"] += 1
                    ans.append("B")
            else:
                if d["A"] > 0:
                    ans.append("A")
                elif d["B"] > 0:
                    ans.append("B")

    if s == "AC":
        if d["A"] > d["C"]:
            d["A"] -= 1
            d["C"] += 1
            ans.append("C")
        elif d["A"] < d["C"]:
            d["C"] -= 1
            d["A"] += 1
            ans.append("A")
        else:
            if d["A"] == d["C"] == 0:
                print("No")
                return
            if N > i + 1:
                if "A" in S[i + 1]:
                    d["C"] -= 1
                    d["A"] += 1
                    ans.append("A")
                elif "C" in S[i + 1]:
                    d["A"] -= 1
                    d["C"] += 1
                    ans.append("C")
                else:
                    d["A"] -= 1
                    d["C"] += 1
                    ans.append("C")
            else:
                if d["A"] > 0:
                    ans.append("A")
                elif d["C"] > 0:
                    ans.append("C")

    if s == "BC":
        if d["B"] > d["C"]:
            d["B"] -= 1
            d["C"] += 1
            ans.append("C")
        elif d["B"] < d["C"]:
            d["C"] -= 1
            d["B"] += 1
            ans.append("B")
        else:
            if d["B"] == d["C"] == 0:
                print("No")
                return
            if N > i + 1:
                if "B" in S[i + 1]:
                    d["C"] -= 1
                    d["B"] += 1
                    ans.append("B")
                elif "C" in S[i + 1]:
                    d["B"] -= 1
                    d["C"] += 1
                    ans.append("C")
                else:
                    d["B"] -= 1
                    d["C"] += 1
                    ans.append("C")
            else:
                if d["B"] > 0:
                    ans.append("B")
                elif d["C"] > 0:
                    ans.append("C")

    if -1 in list(d.values()):
        print("No")
        return

print("Yes")
for a in ans:
    print(a)
