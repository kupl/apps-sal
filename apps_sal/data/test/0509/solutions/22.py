
def main():
    count=int(input())
    arr=[]
    for x in range(count):
        arr.append(int(input()))
    store=[0]
    for x in arr:
        duplicate=[]
        for y in store:
            duplicate.append((y+x)%360)
            duplicate.append((y-x)%360)
        store=duplicate.copy()
    if 0 in store:
        print("YES")
    else:
        print("NO")
main()

