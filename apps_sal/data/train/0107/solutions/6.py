for _ in range(int(input())):
    a, b, c, d = list(map(int, input().split()))
    if (a + b) % 2 == 0:
        if (b != 0 or c != 0) and (a != 0 or d != 0):
            print("Tidak Tidak Ya Ya")
        elif d != 0 or a != 0:
            print("Tidak Tidak Tidak Ya")
        elif b != 0 or c != 0:
            print("Tidak Tidak Ya Tidak")
    else:
        if (b != 0 or c != 0) and (a != 0 or d != 0):
            print("Ya Ya Tidak Tidak")
        elif d != 0 or a != 0:
            print("Ya Tidak Tidak Tidak")
        elif b != 0 or c != 0:
            print("Tidak Ya Tidak Tidak")
