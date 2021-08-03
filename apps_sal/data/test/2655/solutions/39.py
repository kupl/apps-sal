def main():
    N = int(input())
    friendliness = [int(a) for a in input().split(" ")]

    friendliness.sort(reverse=True)
    put = 1
    comfort = 0
    for i in range(len(friendliness)):
        if i == 0:
            put += 1
            comfort += friendliness[0]
        elif put + 2 <= len(friendliness):
            put += 2
            comfort += 2 * friendliness[i]
        else:
            comfort += (len(friendliness) - put) * friendliness[i]
            break

    print(comfort)


main()
