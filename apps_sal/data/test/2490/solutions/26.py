n = "0" + input()
N = len(n)
plus = 1
just = 0
for i in range(1, N):
    plus_plus = plus + 10 - (int(n[i]) + 1)
    plus_just = plus + 10 - int(n[i])
    just_plus = just + 1 + int(n[i])
    just_just = just + int(n[i])

    plus = min(plus_plus, just_plus)
    just = min(just_just, plus_just)

print(just)
