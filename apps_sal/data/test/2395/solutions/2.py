T = int(input())
for _ in range(T):
    s = input()
    if s.count("0") == 0 or s.count("1") == 0:
        print(s)
    else:
        print("01" * len(s))

