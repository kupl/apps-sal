import string

n = int(input())
w = input()
let = set(filter(lambda x: x != '*', w))
ans = None
for _ in range(int(input())):
    v = input()
    check = True
    for c in let:
        check &= not [1 for a, b in zip(w, v) if (a == c) ^ (b == c)]
    if check:
        if ans is None:
            ans = set(v) - let
        ans &= set(v) - let
print(len(ans))
