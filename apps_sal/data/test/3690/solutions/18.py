def main():

    hands = [int(i) for i in input().split()]
    hands[0] *= 5
    hands[3] *= 5
    hands[4] *= 5
    for i in range(5):
        if hands[i] >= 60:
            hands[i] -= 60
    hands[1] += hands[2] / 60
    hands[0] += hands[1] / 60

    t1, t2 = hands[3:]
    hands = hands[:3]
    # print(hands, t1, t2)
    if t1 > t2:
        (t1, t2) = (t2, t1)
    ans1 = True
    ans2 = True
    for t in hands:
        if t > t1 and t < t2:
            ans1 = False
        if (t > t2 and t < 60) or (t >= 0 and t < t1):
            ans2 = False
    # print(ans1, ans2)
    if ans1 or ans2:
        print("YES")
    else:
        print("NO")


def __starting_point():
    main()


__starting_point()
