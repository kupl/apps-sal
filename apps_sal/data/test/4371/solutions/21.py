S = str(input())
Numbers = list(S)
Length = len(Numbers)
Lunlun_choce = []

for i in range(Length - 2):
    choice = Numbers[0:3]
    # print(choice)
    X = "".join(choice)
    number = int(X)
    ans = abs(753 - number)
    Lunlun_choce.append(ans)
    Numbers.pop(0)

print(min(Lunlun_choce))
