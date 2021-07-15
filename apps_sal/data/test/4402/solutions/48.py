def main():
    A,B = list(map(int,input().split()))
    if A >= 13:
        return B
    elif 6 <= A <= 12:
        return int(B/2)
    else:
        return 0

print((main()))

