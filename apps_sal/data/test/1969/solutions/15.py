def main():
    n = int(input())
    matrix = []

    for i in range(n):
        s = input()
        matrix.append(s)

    count = 0

    for i in range(1,n-1):
        for j in range(1,n-1):
            if matrix[i][j] == 'X' and matrix[i-1][j-1] == 'X' and matrix[i-1][j+1] == 'X' and matrix[i+1][j-1] == 'X' and matrix[i+1][j+1] == 'X':
                count += 1
            

    print (count)
    
main()

