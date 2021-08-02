W, H, X, Y = map(int, input().split())
ans_1 = (W * H) / 2
"{:.5f}".format(0.01)
ans_2 = 0
if W / 2 == X and H / 2 == Y:
    ans_2 = 1
print("{:.7f}".format(ans_1), ans_2)
