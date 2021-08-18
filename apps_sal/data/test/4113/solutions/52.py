N = int(input())

cake = 4
donatu = 7

jage = "No"
for d in range(15):
    for c in range(26):
        if cake * c + donatu * d == N:
            jage = "Yes"
print(jage)
