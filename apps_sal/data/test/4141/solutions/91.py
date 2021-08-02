input(); print(['DENIED', 'APPROVED'][all([1, i % 3 == 0 or i % 5 == 0][i % 2 == 0]for i in map(int, input().split()))])
