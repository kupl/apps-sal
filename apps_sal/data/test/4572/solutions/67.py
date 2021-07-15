S = input()

a = [True for _ in range(26)]

for s in S:
    a[ord(s) - ord("a")] = False

for i, aa in enumerate(a):
    if aa:
        print((chr(i + ord("a"))))
        return

print("None")

