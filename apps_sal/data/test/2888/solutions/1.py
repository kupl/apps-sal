# include <iostream>
# include <bits/stdc++.h>
# include <cmath>
using namespace std;
vector<long long> adj[200001];
//bool vis[200001];
/*void dfs (long long s)
{
	vis[s]=true;
	for (long long next : adj[s])
	{
		if (!vis[next])
		{
			dfs(next);
		}
	}
}*/
/*long long bfs(long long s) 
{
    queue<long long> q;
    vector<bool> vis(n);
    long long c = 0;
    vis[s] = true;
    q.push(s);
    while (!q.empty())
	{
        long long currnode = q.front();
        q.pop();
        for (auto next : adj[currnode]) 
		{
            if (!vis[next]) 
			{
                vis[next] = true;
                q.push(next);
            }
        }              
        c++;
    }
    return c;
}*/
long long sdg(long long n)
{
	long long tot=0;
	while (n!=0)
	{
		tot+=n%10;
		n=n/10;
	}
	return tot;
}
long long maxy(long long a, long long b, long long c)
{
	long long arr[3]={a,b,c};
	long long ret_val=*max_element(arr,arr+3);
	return ret_val;
}
int main()
{
	//freopen("time.in","r",stdin); 
	//freopen("time.out","w",stdout);
	
	long long n;
	long long ini_str;
	cin >> n  >> ini_str;
	long long ex[n+1];
	ex[0]=0;
	for (long long i=1;i<=n;i++)
	{
		cin >> ex[i];
	}
	long long str_train[n+1];
	str_train[0]=ini_str;
	for (long long i=1;i<=n;i++)
	{
		long long temp_1=sdg(str_train[i-1]);
		str_train[i]=str_train[i-1]+pow(temp_1,3);
		//cout << i << " " << str_train[i] << endl;
		
	}
	long long dp[n+1][n+1];
	for (long long i=0;i<=n;i++)
	{
		for (long long j=0;j<=n;j++)
		{
			dp[i][j]=0;
		}
	}
	for (long long i=1;i<=n;i++)
	{
		for (long long j=1;j<=i;j++)
		{
			
			// ith city with j trains
			dp[i][j]=max(dp[i-1][j-1],(dp[i-1][j]+(str_train[j-1]*ex[i])));
			//cout << i << " " << j << " " << dp[i][j] << endl;
			
		}
	}
	long long finans=-1e9;
	for (long long i=1;i<=n;i++)
	{
		finans=max(finans,dp[n][i]);
	}
	cout << finans << endl;
	
	// OneDrive\Desktop\rand
	
}												
