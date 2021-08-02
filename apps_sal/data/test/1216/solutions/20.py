n = int(input(""));
a = input("");

i = 0;
cur = '';
count = 0;
while i < n:
    if a[i] != 'a' and a[i] != 'e' and a[i] != 'y' and a[i] != 'u' and a[i] != 'o' and a[i] != 'i':
        print(a[i], end="");
        i = i + 1;
    else:
        cur = a[i];
        count = 0;
        while i < n and a[i] == cur:
            count = count + 1;
            i = i + 1;
        if count == 1:
            print(cur, end="");
        elif count == 2 and (cur == 'o' or cur == 'e'):
            print(cur, end="");
            print(cur, end="");
        else:
            print(cur, end="");
