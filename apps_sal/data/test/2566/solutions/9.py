def main():
    count = int(input())
    for x in range(count):
        lessons = int(input())
        arr = input().split()
        tot = 0
        for y in arr:
            if y == "1":
                tot += 1
        if lessons % tot == 0:
            a = lessons // tot - 1
            b = tot
        else:
            a = lessons // tot
            b = lessons % tot
        store = 7
        for y in range(7):
            test = 0
            for z in range(7):
                if arr[(y + z) % 7] == "1":
                    test += 1
                if test == b:
                    break
            store = min(store, z + 1)
        print(a * 7 + store)


main()
