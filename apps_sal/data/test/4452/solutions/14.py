for t in range(int(input())):
    n = input()
    ans = [n[i] + "0" * (len(n) - i - 1) for i in range(len(n)) if n[i] != "0"]
    print(len(ans))
    print(" ".join(ans))

