# // DP
# // codeforces 489F Special Matrices

n = 0
m = 0
MOD = 0
cap = [0] * 505
ans = [[-1] * 505 for i in range(505)]


def f(one, two):
    if one == 0 and two == 0:
        return 1

    if two > len(ans[one]):
        print(str(one) + ' ' + str(two) + ' ' + len(ans[one]))
    if ans[one][two] != -1:
        return ans[one][two]

    temp = 0
    if two > 1:
        x = two * (two - 1) / 2 * f(one + 2, two - 2)
        temp += x % MOD
    if one > 1:
        x = one * (one - 1) / 2 * f(one - 2, two)
        temp += x % MOD
    if two > 0 and one > 0:
        x = one * two * f(one, two - 1)
        temp += x % MOD
    temp = temp % MOD
    ans[one][two] = temp
    return temp


temp = input().split(' ')
n = int(temp[0])
m = int(temp[1])
MOD = int(temp[2])
for i in range(0, m):
    cur = ''
    cur = input()
    for j in range(0, n):
        if cur[j] == '1':
            cap[j] += 1

n_one = 0
n_two = 0
for i in range(0, n):
    if cap[i] == 0:
        n_two += 1
    if cap[i] == 1:
        n_one += 1

print(int(f(n_one, n_two)))


# // F. Special Matrices
# // time limit per test
# // 1 second
# // memory limit per test
# // 256 megabytes
# // input
# // standard input
# // output
# // standard output

# // An n × n square matrix is special, if:

# //     it is binary, that is, each cell contains either a 0, or a 1;
# //     the number of ones in each row and column equals 2.

# // You are given n and the first m rows of the matrix. Print the number of special n × n matrices, such that the first m rows coincide with the given ones.

# // As the required value can be rather large, print the remainder after dividing the value by the given number mod.
# // Input

# // The first line of the input contains three integers n, m, mod (2 ≤ n ≤ 500, 0 ≤ m ≤ n, 2 ≤ mod ≤ 109). Then m lines follow, each of them contains n characters — the first rows of the required special matrices. Each of these lines contains exactly two characters '1', the rest characters are '0'. Each column of the given m × n table contains at most two numbers one.
# // Output

# // Print the remainder after dividing the required value by number mod.
# // Sample test(s)
# // Input

# // 3 1 1000
# // 011

# // Output

# // 2

# // Input

# // 4 4 100500
# // 0110
# // 1010
# // 0101
# // 1001

# // Output

# // 1

# // Note

# // For the first test the required matrices are:


# // 011
# // 101
# // 110

# // 011
# // 110
# // 101

# // In the second test the required matrix is already fully given, so the answer is 1.
