arr = ["FILIPINO", "JAPANESE", "KOREAN"]

N = int(input())

for _ in range(N):
    line = input()
    if line[-2:] == "po":
        print(arr[0])
    if line[-4:] == "desu" or line[-4:] == "masu":
        print(arr[1])
    if line[-5:] == "mnida":
        print(arr[2])
