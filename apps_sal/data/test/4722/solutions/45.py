a, b = map(int, input().split())
# intは入力に対しての関数、出力ではない

if (a+b)%3 == 0:
    print("Possible")
elif a%3 == 0:
    print("Possible")
elif b%3 == 0:
    print("Possible")
else:
    print("Impossible")
