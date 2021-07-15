def main():
    N = int(input())
    for i in range(N):
        a = input().strip()
        if a.endswith("po"):
            print("FILIPINO")
        elif a.endswith("mnida"):
            print("KOREAN")
        else:
            print("JAPANESE")

main()

