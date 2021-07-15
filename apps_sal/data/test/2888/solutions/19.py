

int long
max(int long a, int long b)
{
        return a>b ? a:b;
}

int long
digcube(int long n)
{
        int long t = n;
        int sum;
        for (sum = 0; t > 0; sum += t % 10, t /= 10);
        return sum*sum*sum;
}

int
main()
{
        int n,i,j;
        int long s;
        scanf("%d %ld", &n, &s);
        int e[n];
        for(i=0;i<n;i++)
                scanf("%d", &e[i]);
        int long strength[n];
        strength[0] = s;
        int long table[n][n];
        for(i=1;i<n;i++)
                strength[i] = strength[i-1] + digcube(strength[i-1]);
        for(i=0;i<n;i++)
                table[n-1][i] = strength[i] * e[n-1];
        for(i=n-2; i>=0; i--)
        {
                for(j=0; j<=i;j++)
                        table[i][j] = max((strength[j] * e[i] + table[i+1][j]), table[i+1][j+1]);
        }
        printf("%ld", table[0][0]);
        return 0;
}
 

