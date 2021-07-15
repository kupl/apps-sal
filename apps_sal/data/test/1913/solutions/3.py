def yep(s):
    return (s[0] == "1" and s[1:] == "0" * (len(s) - 1))

def main():
    n = int(input())
    arr = list(map(str, input().split()))
    sm = 0
    ann = 0
    for i in range(n):
        if (arr[i] == "0"):
            print(0)
            return
        if yep(arr[i]):
            sm += len(arr[i]) - 1
        else:
            ann = arr[i]
    if (ann == 0):
        print("1" + "0" * sm)
    else:
        print(ann, "0" * sm, sep = "")

main()
