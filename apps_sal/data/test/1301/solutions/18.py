def main():
    a = ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]
    n = int(input())
    s = input()
    for name in a:
        if len(name) == len(s):
            good = True
            for i in range(len(s)):
                if s[i] != '.':
                    if name[i] != s[i]:
                        good = False
                        break
            if good:
                print(name)
    
main()
