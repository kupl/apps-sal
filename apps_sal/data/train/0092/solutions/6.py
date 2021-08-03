for _ in range(int(input())):
    line1 = input()
    line2 = input()
    if set(line1) & set(line2):
        print("YES")
    else:
        print("NO")
