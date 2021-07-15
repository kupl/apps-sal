from collections import defaultdict

n = int(input())
inf = float('inf')
mins = defaultdict(lambda: inf)
for _ in range(n):
    ci, vit = input().split()
    ci = int(ci)
    vit = "".join(sorted(vit))
    mins[vit] = min(mins[vit], ci)

result = min(
    mins["A"] + min(min(mins["B"], mins["AB"]) + min(mins["C"], mins["AC"]), mins["BC"]),
    mins["B"] + min(min(mins["A"], mins["AB"]) + min(mins["C"], mins["BC"]), mins["AC"]),
    mins["C"] + min(min(mins["A"], mins["AC"]) + min(mins["B"], mins["BC"]), mins["AB"]),
    mins["AB"] + min(mins["C"], mins["AC"], mins["BC"]),
    mins["AC"] + min(mins["B"], mins["AB"], mins["BC"]),
    mins["BC"] + min(mins["A"], mins["AB"], mins["AC"]),
    mins["ABC"],
)
print(-1 if result == inf else result)

