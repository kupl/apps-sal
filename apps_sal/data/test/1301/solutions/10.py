S = ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]
n = int(input())
s = input()
for x in S :
    if (len(x) == n) : 
        for a, b in zip(x, s):
            if b != '.' and a != b :
                break;
        else :
            print(x);
            break;

