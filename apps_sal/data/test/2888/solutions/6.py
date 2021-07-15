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
vector<string> actions={"train", "fight"};
vector<long long> ex;
vector<long long> all_ans;
long long finans=-1e9;
void bfs(long long totcity,long long city, long long st, long long exp)
{
	queue<tuple<long long, long long , long long> > q;
	q.push({city,st,exp});
	bool vis1[100000]={false};
	bool vis2[100000]={false};
	bool stopwhile=false;
	while (!q.empty())
	{
		//cout << "still going " << q.size() << endl;
		tuple<long long , long long, long long> curr_tuple=q.front();
		long long curr_city=get<0>(curr_tuple);
		long long curr_str=get<1>(curr_tuple);
		long long curr_exp=get<2>(curr_tuple);
		vis1[curr_exp]=true;
		vis2[curr_str]=true;
		//finans=max(finans,curr_exp);
		q.pop();
		long long nex_str=0;
		long long nex_exp=0;
		long long nex_city=0;
		for (auto action : actions)
		{
			if (action=="train")
			{
				nex_str=curr_str+pow(sdg(curr_str),3);
				nex_exp=curr_exp;
				nex_city=curr_city+1;
			}
			else if (action=="fight")
			{
				nex_str=curr_str;
				nex_city=curr_city+1;
				nex_exp=curr_exp+(curr_str*ex[nex_city]);
			}
			//cout << action << " " << nex_city << " " << nex_str << " " << nex_exp << endl;
			bool chec=(!vis1[nex_exp] || !vis2[nex_str]);
			if ((nex_city<=totcity))
			{
				//cout << action << " " << nex_city << " " << nex_str << " " << nex_exp << endl;
				q.push({nex_city,nex_str,nex_exp});
				//vis1[nex_exp]=true;
				//vis2[nex_str]=true;
				all_ans.push_back(nex_exp);
				//finans=max(finans,nex_exp);
			}
		}
		/*if (((!vis1[nex_exp]) || (!vis2[nex_str])) && (nex_city<=totcity))
		{
			q.push({nex_city,nex_str,nex_exp});
			vis1[nex_exp]=true;
			vis2[nex_str]=true;
		}*/
	}
	
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
	cin >> n >> ini_str;
	ex.push_back(0);
	for (long long i=1;i<=n;i++)
	{
		long long lol;
		cin >> lol;
		ex.push_back(lol);
	}
	bfs(n, 0, ini_str,0);
	cout << *max_element(all_ans.begin(),all_ans.end());
	
	// OneDrive\Desktop\rand
	
}												
