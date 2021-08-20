n = int(input(''))
k = int(input(''))
a = int(input(''))
b = int(input(''))
ans = 0
while not n == 1:
    m = n % k
    n = n - m
    ans = ans + m * a
    if (n - n / k) * a > b:
        n = n / k
        ans = ans + b
    else:
        ans = ans + (n - 1) * a
        n = 1
print(int(ans))
'\n\tint64 ans = 0;\n\twhile(n != 1){\n\t\tint64 m = n % k;\n\t\tn -= m;\n\t\t//cout << "m " << m << endl;\n\t\tans += m*a;\n\n\t\tif((n-(n/k))*a > b){\n\t\t\tn /= k;\n\t\t\tans += b;\n\t\t}else{\n\t\t\tans += (n-1)*a;\n\t\t\tcout << ans;\n\t\t\treturn 0;\n\t\t}\n\n\t}\t\n\t\n\tcout << ans;\n'
