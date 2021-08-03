ar = list(input())
while True:
    a = len(ar)
    if a == 0:
        print("YES")
        break
    if "".join(ar[a - 5:a]) == "dream" or "".join(ar[a - 5:a]) == "erase":
        del ar[a - 5:a]
    elif "".join(ar[a - 6:a]) == "eraser":
        del ar[a - 6:a]
    elif "".join(ar[a - 7:a]) == "dreamer":
        del ar[a - 7:a]
    else:
        print("NO")
        break
