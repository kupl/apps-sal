cnt = int(input())
string = input()

if len(string) <= cnt:
    print(string)
else:
    print(string[:cnt] + "...")
